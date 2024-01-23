<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-8">
        <div class="main-left">
            <div class="p-12 bg-green-200 border border-gray-200 rounded-xl">
                <h1 class="mb-6 text-2xl">Регистрация</h1>

                <p class="mb-4 text-gray-600">
                    Вы должны зарегистрироваться, чтобы использовать этот сервис.
                    Присоединяйтесь к нашему сообществу, общайтесь и делитесь своими интересами с другими людьми.
                </p>

                <p class="font-bold">
                    Уже есть аккаунт? <RouterLink :to="{'name': 'login'}" class="underline">Нажмите здесь</RouterLink>, чтобы войти!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-green-200 border border-gray-200 rounded-xl">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Имя</label><br>
                        <input type="text" v-model="form.name" placeholder="Введите ваше имя" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <label>Фамилия</label><br>
                        <input type="text" v-model="form.surname" placeholder="Введите вашу фамилию" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Введите ваш e-mail" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <label>Пароль</label><br>
                        <input type="password" v-model="form.password1" placeholder="Введите пароль" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <label>Повторите пароль</label><br>
                        <input type="password" v-model="form.password2" placeholder="Введите пароль ещё раз" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-400 text-white rounded-xl p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-violet-600 text-white rounded-xl">Зарегистрироваться</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                surname: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Вы не ввели ваш e-mail')
            }

            if (this.form.name === '') {
                this.errors.push('Вы не ввели ваше имя')
            }

            if (this.form.surname === '') {
                this.errors.push('Вы не ввели вашу фамилию')
            }

            if (this.form.password1 === '') {
                this.errors.push('Вы не ввели пароль')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('Пароли не совпадают')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Пользователь зарегистрирован. Пожалуйста, войдите в аккаунт', 'bg-emerald-400')

                            this.$router.push('/login')
                        } else {
                            this.toastStore.showToast(5000, 'Что-то пошло не так. Пожалуйста, повторите ещё раз', 'bg-red-400')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>