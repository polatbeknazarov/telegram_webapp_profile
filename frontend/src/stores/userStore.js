import { defineStore } from "pinia";

import { api } from "./../utils/api"


export const useUserStore = defineStore("user", {
    state: () => ({
        userData: null,
    }),
    actions: {
        async fetchUser(telegram_id, first_name, username = null, last_name = null) {
            try {
                let data = await api.getUser(telegram_id);

                this.userData = data;
            } catch (error) {
                if (error.response && error.response.status === 404) {
                    this.userData = await api.createUser(telegram_id, username, first_name, last_name);
                } else {
                    console.error("Error get_or_create user::", error);
                    throw error;
                }
            }
        },
        async setBirthDate(telegram_id, birth_date) {
            try {
                this.userData = await api.setBirthDate(telegram_id, birth_date)
            } catch (error) {
                console.error("Error updating user:", error);
                throw error
            }
        },
    },
});
