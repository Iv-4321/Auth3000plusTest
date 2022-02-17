<template>
<div class="nav-scroller py-1 mb-2">
    <div class="nav d-flex justify-content-between">
        <input v-model="keyword" class="form-control" type="text" placeholder="Search" aria-label="Search">
        <div v-bind:key="result.id" v-for="result in results">
              <div class="album py-5 bg-light">
          <div class="container">
                 <div class="card mb-4 box-shadow">
                            <img :src="result.picture" fluid />
                  <div class="card-body">
                      <h4 class=""><a class="text-secondary" href="">{{result.name}}</a></h4>
                      <p class="card-text">{{result.author}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                      <a href="" class="btn btn-sm btn-outline-primary" @click.prevent="getpdf(result.pdf)" role="button" aria-pressed="true">Читать книгу</a>

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
import { getAPI } from '../axios-api';


export default {
  name: 'Search',
  components: {
  },
  data() {
      return {
          keyword: '',
          results: [],
      }
  },
  watch: {
    keyword: function(newVal) {
      if (newVal.length >2) {
        this.getResults();
      }
    }
  },

  methods: {
      getpdf(file) {
          window.open("" + file, "");
      },
      getResults() {
          getAPI.get("/api/books/?search="+this.keyword)
          .then(res => (this.results = res.data))
          .catch(err => console.log(err));
      }
      },
      created() {
      this.getResults()
      }



}
</script>