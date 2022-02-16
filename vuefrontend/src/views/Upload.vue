<template>
    <v-container>

            <v-file-input label="Insert PDF Book" truncate-length="70" accept=".pdf" v-model="pdf" />

            <v-col>
                <v-text-field
                  v-model="name"
                  color="purple darken-2"
                  label="Enter book title"
                  required
                ></v-text-field>
            </v-col>

            <v-col>
                <v-text-field
                  v-model="author"
                  color="blue darken-2"
                  label="Write an author"
                  required
                ></v-text-field>
            </v-col>

            <v-file-input label="Insert picture Book" truncate-length="70" accept=".png" v-model="picture" />
            <div class="large-12 medium-12 smayll-12 cell">
            <v-btn v-on:click="addFile()">Add Book</v-btn>
            </div>

    </v-container>

</template>

<script>
import axios from 'axios'

  export default {
    data(){
      return {
        pdf: null,
        name: '',
        author: '',
        picture: '',
        search_term: '',
      }
    },
    methods: {

      addFile(){
        let formData = new FormData();
          formData.append('pdf', this.pdf);
          formData.append('name', this.name);
          formData.append('author', this.author);
          formData.append('picture', this.picture);
          console.log(FormData);

        axios.post( 'http://127.0.0.1:8000/api/books/', formData)

            .then((response) => {
                        console.log(response);
                        console.log(formData);

                    })
                    .catch((error) => {
                        console.log(error);
                    });

      },

        }
    }

</script>

<style lang="scss">
/*    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;

        a {
            font-weight: bold;
            color: #2c3e50;

            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }*/
</style>