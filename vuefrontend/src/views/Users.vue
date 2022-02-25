<template>
<div class="users">
      <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <div v-for="user in APIData" :key="user.username" :to="user.useremail" class="col-md-4">
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

            console.log(response.data);
          })
          .catch(err => {
            console.log(err)
          })
    },
    }

</script>