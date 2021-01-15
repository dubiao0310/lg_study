<template>
    <div class="regiset">
        <h1>注册</h1>
        <v-text-field v-model="username" dense label="用户名"></v-text-field>
        <v-text-field v-model="password" dense label="密码" type='password'></v-text-field>
        <v-btn color="warning" @click="register()" dark>注册</v-btn>
        <v-btn color="primary" @click="singin()" text>去登陆</v-btn>
    
    </div>
</template>

<script>
export default {
    data() {
        return { 
            username: "",
            password: ""
        }
    },
    methods: {
        singin(){
            this.$router.push({name: "singin"})
        },
        register(){
            let post_data = {
                username: this.username,
                password: this.password
            }
            this.$api.user.register(post_data).then(res=>{
                console.log(res)
            })
        }
    },
    
}
</script>

<style scoped>

</style>