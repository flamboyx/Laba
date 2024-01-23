<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-8">
        <div class="main-left col-span-3 space-y-4">
            <div class="bg-green-200 border border-gray-200 rounded-xl">
                <form v-on:submit.prevent="submitForm" class="p-4 flex space-x-4">
                    <input v-model="query" type="search" class="p-4 w-full bg-gray-100 rounded-xl" placeholder="Что вы хотите найти?">

                    <button href="#" class="inline-block py-4 px-6 bg-violet-600 text-white rounded-xl">Искать</button>
                </form>
            </div>

            <div class="p-4 bg-green-100 border border-gray-200 rounded-xl grid grid-cols-4 gap-4">
                <div class="p-4 text-center bg-gray-100 rounded-xl"
                     v-for="user in users"
                    v-bind:key="user.id"
                >
                    <img src="https://i.pravatar.cc" class="mb-6 rounded-tr-3xl rounded-b-xl">
                
                    <p class="text-lg"><strong>{{ user.name + ' ' + user.surname}}</strong></p>

                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-sm text-gray-500">105 друзей</p>
                        <p class="text-sm text-gray-500">65 постов</p>
                    </div>
                </div>
            </div>



        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />

            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'

export default {
    name: 'SearchView',

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
    },

    data() {
        return {
            query: '',
            users: [],
            posts: []
        }
    },

    methods: {
        submitForm() {
            console.log('submitForm', this.query)

            axios
                .post('/api/search/', {
                    query: this.query
                })
                .then(response => {
                    console.log('response:', response.data)

                    this.users = response.data.users
                    this.posts = response.data.posts
                })
                .catch(error => {
                    console.log('error:', error)
                })
        }
    }
}
</script>