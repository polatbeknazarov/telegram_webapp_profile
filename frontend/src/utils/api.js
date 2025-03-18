import axios from 'axios';

const BASE_URL = 'https://example.com/api/v1';

export const api = {
    createUser: async (telegram_id, username = null, first_name, last_name = null) => {
        const { data } = await axios.post(`${BASE_URL}/users`, {
            telegram_id: telegram_id,
            username: username,
            first_name: first_name,
            last_name: last_name,
        });

        return data;
    },
    getUser: async (telegram_id) => {
        const { data } = await axios.get(`${BASE_URL}/users/${telegram_id}`, {
            params: { telegram_id: telegram_id },
            headers: {
                "ngrok-skip-browser-warning": "69420",
            },
        });

        return data;
    },
    setBirthDate: async (telegram_id, birth_date) => {
        const { data } = await axios.patch(
            `${BASE_URL}/users/set_birth_date`, { telegram_id: telegram_id, birth_date: birth_date },
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });
        return data;
    }
};
