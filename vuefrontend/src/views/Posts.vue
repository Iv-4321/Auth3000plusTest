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
                      <a href="" class="btn btn-sm btn-outline-primary" @click.prevent="getPdf(book.pdf)" role="button" aria-pressed="true">Читать книгу</a>
                      </div>
                      <small class="text-muted">9 mins</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
      <v-pagination v-model="currentPage"
        :length="6"
        >
      </v-pagination>
  </div>
</template>

<script>

  import { getAPI } from '../axios-api'
  import { mapState } from 'vuex'
  export default {
    name: 'Book',
    data() {
        return {
        numberOfPages: 1,
        currentPage: 1,
        data: [],
        chosenBook: null,
        };
    },



    components: {

    },
    computed: mapState(['APIData']),

    created() {
            this.GetAllBooksOnPage();

        },
        watch: {
        },


    //created () {

        //this.onPageChange(this.currentPage); //активирует работу кнопок пагинации на стр
        //console.log(this.currentPage)
        //getAPI.get('/api/books/')
          //.then(response => {
            //this.$store.state.APIData = response.data
          //})
          //.catch(err => {
           // console.log(err)
          //})
    //},

    methods: {
        GetAllBooksOnPage() {
                getAPI.get('http://127.0.0.1:8000/api/books/?page='+this.currentPage)
          .then(response => {
            this.$store.state.APIData = response.data
            console.log(response.data)
            console.log(this.currentPage)
          })
          .catch(err => {
            console.log(err)
          })
        },

        getPdf(file) {
            window.open("" + file, "");
        }

      },
    }

</script>

<style>

</style>
