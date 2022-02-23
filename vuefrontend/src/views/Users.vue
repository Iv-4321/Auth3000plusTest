<template>
<div class="users">
      <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <div v-for="user in APIData" :key="user.id" :to="user.username" class="col-md-4">
                      <h4 class=""><a class="text-secondary" href="">{{user.username}}</a></h4>
              </div>
            </div>
          </div>
      </div>
</div>
</template>

<script>

  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'
  import Cookies from 'js-cookie'

  export default {
    name: 'Users',
    data() {
        return {
        data: []
        };
    },



    components: {

    },
    computed: mapState(['APIData']),


    created () {
        getAPI.get('/auth/users/')
          .then(response => {
            this.$store.state.APIData = response.data

            Cookies.set('Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NjEzNzcwLCJqdGkiOiJiMTdhMDU2ZWNlNGY0N2QxYTFjNWZiYmFlMDY1MjQ2MiIsInVzZXJfaWQiOjF9.7u4S1XKoI8sTh1JiIcBp5-yc7pS6OJHMZS1cTU1qDqU', response.data);

            console.log(response.data);
          })
          .catch(err => {
            console.log(err)
          })
    },
    }

</script>