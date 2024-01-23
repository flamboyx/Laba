<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-8">
        <div class="main-left">
            <div class="p-12 bg-green-200 border border-gray-200 rounded-xl">
                <h1 class="mb-6 text-2xl">Вход</h1>

                <p class="mb-4 text-gray-600">
                    Войдите в свой аккаунт.
                </p>

                <p class="font-bold">
                    У вас нет аккаунта? <RouterLink :to="{'name': 'signup'}" class="underline">Нажмите здесь</RouterLink>, чтобы создать его!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-green-200 border border-gray-200 rounded-xl">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Введите ваш e-mail" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <label>Пароль</label><br>
                        <input type="password" v-model="form.password" placeholder="Введите ваш пароль" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-violet-600 text-white rounded-xl">Войти</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Вы не ввели ваш e-mail')
            }

            if (this.form.password === '') {
                this.errors.push('Вы не ввели ваш пароль')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        console.log(response.data.access)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)
                    })

                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>