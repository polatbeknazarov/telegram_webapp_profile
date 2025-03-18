<template>
  <div
    class="h-screen flex flex-col justify-between bg-gradient-to-b from-blue-600 to-purple-800 text-white px-5 py-10">
    <Loader v-if="isLoading" />

    <h1 class="text-2xl font-bold text-center">Введи свою дату рождения</h1>

    <div class="flex justify-center items-center space-x-4">
      <select v-model="selectedDay" class="p-5 bg-white bg-opacity-10 rounded-lg shadow-md focus:outline-none">
        <option v-for="day in days" :key="day" :value="day">{{ day }}</option>
      </select>
      <select v-model="selectedMonth" class="p-5 bg-white bg-opacity-10 rounded-lg shadow-md focus:outline-none">
        <option v-for="(month, index) in months" :key="index" :value="index">{{ month }}</option>
      </select>
      <select v-model="selectedYear" class="p-5 bg-white bg-opacity-10 rounded-lg shadow-md focus:outline-none">
        <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
      </select>
    </div>

    <div class="w-full">
      <button @click="submitDate" :disabled="isLoading"
        class="w-full py-4 bg-white bg-opacity-10 text-white font-semibold rounded-xl shadow-md hover:bg-gray-300 disabled:opacity-50">
        {{ isLoading ? "Сохранение..." : "Продолжить" }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "./../stores/userStore";
import Loader from "../components/Loader.vue";

const store = useUserStore();
const router = useRouter()
const isLoading = ref(false);

const months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
const years = Array.from({ length: 50 }, (_, i) => new Date().getFullYear() - i);

const selectedYear = ref(years[0]);
const selectedMonth = ref(0);
const selectedDay = ref(1);

const daysInMonth = computed(() => new Date(selectedYear.value, selectedMonth.value + 1, 0).getDate());
const days = computed(() => Array.from({ length: daysInMonth.value }, (_, i) => i + 1));

const submitDate = async () => {
  isLoading.value = true;

  try {
    const birthDate = `${selectedYear.value}-${String(selectedMonth.value + 1).padStart(2, "0")}-${String(selectedDay.value).padStart(2, "0")}`;

    await store.setBirthDate(store.userData.telegram_id, birthDate);
    router.push(`/profile/${store.userData.telegram_id}`)
  } catch (error) {
    console.error("Error updating birth_date:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
select {
  appearance: none;
  cursor: pointer;
}
</style>
