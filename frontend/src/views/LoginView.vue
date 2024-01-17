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
                <form class="space-y-6">
                    <div>
                        <label>E-mail</label><br>
                        <input type="email" placeholder="Введите ваш e-mail" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <label>Пароль</label><br>
                        <input type="password" placeholder="Введите ваш пароль" class="w-full mt-2 py-4 px-6 border border-gray-100 rounded-xl">
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-violet-600 text-white rounded-xl">Войти</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>