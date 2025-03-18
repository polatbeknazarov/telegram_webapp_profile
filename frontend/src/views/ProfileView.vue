<template>
    <div
        class="h-screen flex flex-col justify-between bg-gradient-to-b from-blue-600 to-purple-800 text-white px-5 py-10">
        <Loader v-if="isLoading" />

        <h1 class="text-4xl text-center mb-5">{{ randomEmoji }}</h1>

        <div class="flex flex-col items-center" v-if="profileData">
            <p class="text-2xl font-bold">
                {{ profileData.first_name }} {{ profileData.last_name }}
            </p>
            <p class="text-white text-opacity-40 mb-10">@{{ profileData.username }}</p>
            <p class="text-lg font-semibold">До дня рождения осталось</p>
            <p class="text-5xl font-extrabold">{{ timeUntilBirthday }} дней</p>
        </div>

        <div v-if="!isLoading">
            <button @click="isOwnProfile ? navigateToBirthDateForm() : navigateToMainMenu()"
                class="w-full py-4 bg-white bg-opacity-10 text-white font-semibold rounded-xl shadow-md hover:bg-gray-300">
                {{ isOwnProfile ? "Изменить" : "Главное меню" }}
            </button>

            <button v-if="isOwnProfile" @click="shareProfile"
                class="w-full mt-4 py-4 bg-white bg-opacity-10 text-white font-semibold rounded-xl shadow-md hover:bg-gray-300">
                Поделиться
            </button>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, ref, toRef } from "vue";
import { useRoute, useRouter } from "vue-router";
import { api } from "../utils/api";
import { randomEmoji } from "../utils/getRandomEmoji";
import { useUserStore } from "../stores/userStore";
import Loader from "../components/Loader.vue";

const route = useRoute();
const router = useRouter();
const store = useUserStore();
const profileData = ref(null);
const isLoading = ref(true);

const telegramId = toRef(route.params, "telegram_id");

onMounted(async () => {
    try {
        profileData.value = await api.getUser(telegramId.value);
    } catch (error) {
        console.error("Error get profile:", error);
    } finally {
        isLoading.value = false;
    }
});

const timeUntilBirthday = computed(() => {
    if (!profileData.value?.birth_date) return "...";

    const now = new Date();
    const birthDate = new Date(profileData.value.birth_date);
    let nextBirthday = new Date(now.getFullYear(), birthDate.getMonth(), birthDate.getDate());

    if (nextBirthday < now) {
        nextBirthday.setFullYear(nextBirthday.getFullYear() + 1);
    }

    return Math.ceil((nextBirthday - now) / (1000 * 60 * 60 * 24));
});

const isOwnProfile = computed(() => profileData.value?.telegram_id === store.userData.telegram_id);

const shareProfile = () => {
    const payload = encodeURIComponent(profileData.value.telegram_id);
    const shareUrl = `https://t.me/share/url?url=${encodeURIComponent(`https://t.me/polat_testovoe_bot?startapp=${payload}`)}`;
    window.Telegram.WebApp.openTelegramLink(shareUrl);
};

const navigateToBirthDateForm = () => router.push("/");
const navigateToMainMenu = () => router.push("/");
</script>
