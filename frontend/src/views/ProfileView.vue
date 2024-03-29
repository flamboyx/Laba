<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-green-200 border border-gray-200 text-center rounded-xl">
                <img :src="user.get_avatar" class="mb-6 rounded-tr-3xl rounded-b-xl">
                
                <p><strong>{{ user.name + ' ' + user.surname}}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{name: 'friends', params: {id: user.id}}" class="text-sm text-gray-600">{{ user.friends_count }} друзей</RouterLink>
                    <p class="text-sm text-gray-600">{{ user.posts_count }} постов</p>
                </div>

                <div class="mt-6">
                    <button class="inline-block py-4 px-3 bg-violet-600 text-sm text-white rounded-xl"
                        @click="sendFriendshipRequest"
                        v-if="userStore.user.id !== user.id"
                    >
                        Добавить в друзья
                    </button>

                    <button 
                        class="inline-block mt-4 py-4 px-3 bg-violet-600 text-sm text-white rounded-xl"
                        @click="sendDirectMessage"
                        v-if="userStore.user.id !== user.id"
                    >
                        Отправить сообщение
                    </button>

                    <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-violet-600 text-sm text-white rounded-xl"
                        to="/profile/edit"
                        v-if="userStore.user.id === user.id"
                    >
                        Изменить профиль
                    </RouterLink>

                    <button 
                        class="inline-block py-4 px-3 bg-red-400 text-sm text-white rounded-xl"
                        @click="logout"
                        v-if="userStore.user.id === user.id"
                    >
                        Выйти
                    </button>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div 
                class="bg-green-200 border border-gray-200 rounded-xl"
                v-if="userStore.user.id === user.id"
            >
                <FeedForm 
                    v-bind:user="user" 
                    v-bind:posts="posts"
                />
            </div>

            <div 
                class="p-4 bg-green-100 border border-gray-200 rounded-xl"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" v-on:deletePost="deletePost"/>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />

            <Trends />
        </div>
    </div>
</template>

<style>
input[type="file"] {
    display: none;
}

.custom-file-upload {
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
</style>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import FeedForm from '../components/FeedForm.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
        FeedForm
    },

    data() {
        return {
            posts: [],
            user: {
               id: null
            },
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: {
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        deletePost(id) {
            this.posts = this.posts.filter(post => post.id !== id)
        },

        sendDirectMessage() {
            console.log('sendDirectMessage')

            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/chat')
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    console.log('data', response.data)

                    if (response.data.message === 'request already sent') {
                        this.toastStore.showToast(5000, 'Запрос в друзья уже был отправлен', 'bg-red-400')
                    } else {
                        this.toastStore.showToast(5000, 'Запрос в друзья был отправлен', 'bg-emerald-400')
                    }
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        logout() {
            console.log('Log out')

            this.userStore.removeToken()

            this.$router.push('/login')
        }
    }
}
</script>