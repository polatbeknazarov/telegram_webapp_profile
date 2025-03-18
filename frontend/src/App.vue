<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script setup>
import { onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "./stores/userStore";

const store = useUserStore();
const router = useRouter();

onMounted(async () => {
  if (!window.Telegram?.WebApp) return;

  const tg = window.Telegram.WebApp;
  tg.expand();

  const tgUser = tg.initDataUnsafe?.user;
  const startParam = tg.initDataUnsafe?.start_param;

  if (tgUser) {
    try {
      await store.fetchUser(
        tgUser.id,
        tgUser.first_name,
        tgUser.username ? tgUser.username : null,
        tgUser.last_name ? tgUser.last_name : null
      );
    } catch (error) {
      console.error("Error get_or_create user:", error);
      return;
    }
  }

  if (startParam) {
    router.push(`/profile/${startParam}`);
  }
});

watch(() => store.userData?.birth_date, (birthDate) => {
  if (birthDate) {
    router.push(`/profile/${store.userData.telegram_id}`);
  }
});
</script>
