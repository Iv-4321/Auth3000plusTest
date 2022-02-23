<template>
    <v-card>
        <v-toolbar>
            <v-icon>
                mdi-account
            </v-icon>
            <v-toolbar-title>Register</v-toolbar-title>
        </v-toolbar>
        <v-card-title></v-card-title>
        <v-card-text>
            <v-text-field label="Email"
                          clearable
                          v-model="email"
                          :rules="emailRules"
                          suffix="@gmail.com">
            </v-text-field>
            <v-text-field label="Username"
                          clearable
                          v-model="username"
                          :rules="usernameRules">
            </v-text-field>
            <v-text-field label="Password"
                          type="password"
                          clearable
                          v-model="password"
                          :rules="passwordRules">
            </v-text-field>
        </v-card-text>
        <v-card-actions>
            <v-btn @click="Register"
                   large>
                Register
                <v-icon right>
                    mdi-login-variant
                </v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    import axios from 'axios'

export default {
  name: "Register",
  components: {
  },
  data() {
      return {
          email: null,
          username: null,
          password: null,
          emailRules: [
              n => !!n || 'Email is required',
          ],
          usernameRules: [
              u => !!u || 'Username is required',
          ],
          passwordRules: [
              p => !!p || 'Password is required',
              p => (p && p.length >= 6) || 'Password must be longer than 6 characters'
          ],
    }
  },
        created() {
  },
  computed: {
  },
  methods: {
      Register() {

          let formData = new FormData();
          formData.append('email', this.email);
          formData.append('username', this.username);
          formData.append('password', this.password);
          axios.post("http://127.0.0.1:8000/auth/users/", formData)
              .then(response => {
                  if (response.statusText == "No Content") {
                      alert("Some error occure, try again");
                  }
                  else {
                      console.log(response);
                      this.$router.push('/');
                  }
              })
              .catch(error => {
                  console.log(error);
              })
              .then(function () {
              });
      }
      },
}
</script>

<style>
</style>