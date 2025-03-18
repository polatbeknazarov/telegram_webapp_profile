import { createRouter, createWebHistory } from "vue-router";

import ProfileView from "./../views/ProfileView.vue";
import BirthDateForm from "./../views/BirthDateForm.vue";

const routes = [
    { path: "/", component: BirthDateForm },
    { path: "/profile/:telegram_id?", component: ProfileView },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
