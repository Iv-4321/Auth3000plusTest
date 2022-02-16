<template>
   <div class="search-field">
                <input class="text"
                 type="search-field"
                 v-model="searchValue"
                >
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit" @click="search(searchValue)">Search</button>
   </div>
</template>

<script>
    export default {
        name: "Search",
        props: {},
        data() {
            return {
             searchValue: ''
            }
        },
        methods: {
         search() {

         }
        }
    }

</script>