<template>
    <v-container>
      <div class="container">
        <div class="large-12 medium-12 small-12 cell">
          <label>PDF
            <v-file-input label="Insert PDF Book" truncate-length="70" accept=".pdf" v-model="pdf" />
          </label>
          <label>Name
            <v-col>
            <v-text-field
              v-model="name"
              color="purple darken-2"
              label="Enter book title"
              required
            ></v-text-field>
          </v-col>
          </label>
          <label>Author
          <v-col>
            <v-text-field
              v-model="author"

              color="blue darken-2"
              label="Write an avatar"
              required
            ></v-text-field>
          </v-col>
          </label>
          <label>Description
          <v-col>
            <v-text-field
              v-model="description"

              color="blue darken-2"
              label="Write a description"
              required
            ></v-text-field>
          </v-col>
          </label>

            <div class="large-12 medium-12 smayll-12 cell">
            <v-btn v-on:click="addFile()">Add Book</v-btn>
            </div>
        </div>
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
        description: '',
      }
    },
    methods: {

      addFile(){
        let formData = new FormData();
          formData.append('pdf', this.pdf);
          formData.append('name', this.name);
          formData.append('author', this.author);
          formData.append('description', this.description);
          console.log(FormData);

        axios.post( 'http://127.0.0.1:8000/api/books/', formData)
            .then((response) => {
                        console.log(response);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
      }
    }
  }
</script><template>
    <v-container>
      <div class="container">
        <div class="large-12 medium-12 small-12 cell">
          <label>PDF
            <v-file-input label="Insert PDF Book" truncate-length="70" accept=".pdf" v-model="pdf" />
          </label>
          <label>Name
            <v-col>
            <v-text-field
              v-model="name"
              color="purple darken-2"
              label="Enter book title"
              required
            ></v-text-field>
          </v-col>
          </label>
          <label>Author
          <v-col>
            <v-text-field
              v-model="author"

              color="blue darken-2"
              label="Write an avatar"
              required
            ></v-text-field>
          </v-col>
          </label>

          <label>Picture
            <v-file-input label="Insert picture Book" truncate-length="70" accept=".png" v-model="picture" />
          </label>

            <div class="large-12 medium-12 smayll-12 cell">
            <v-btn v-on:click="addFile()">Add Book</v-btn>
            </div>
        </div>
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
                    })
                    .catch((error) => {
                        console.log(error);
                    });
      }
    }
  }
</script>