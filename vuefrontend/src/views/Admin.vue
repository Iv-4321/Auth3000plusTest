<template>
  <div class="book">

      <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <div v-for="book in APIData" :key="book.id" :to="book.pdf" class="col-md-4">
                <div class="card mb-4 box-shadow">
                            <img :src="book.picture" fluid />
                  <div class="card-body">
                      <h4 class=""><a class="text-secondary" href="">{{book.name}}</a></h4>
                      <p class="card-text">{{book.author}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                      <a href="" class="btn btn-sm btn-outline-primary" @click.prevent="getpdf(book.pdf)" role="button" aria-pressed="true">Читать книгу</a>
                      </div>
                      <div class="btn-group">
                      <a href="" class="btn btn-danger" role="button" aria-pressed="true">Удалить</a>
                      </div>

                      <small class="text-muted">9 mins</small>
                    </div>
                  </div>
                </div>
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
    name: 'Book',
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    components: {
    },
    computed: mapState(['APIData']),
    created () {
        getAPI.get('http://127.0.0.1:8000/api/books/')
          .then(response => {
            this.$store.state.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    },
    methods: {
        getpdf(file) {
            window.open("" + file, "");
        }
    }
  }
</script>

<style>
</style>
