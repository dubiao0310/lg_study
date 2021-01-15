<template>
    <div class="singin">
        <h1>登录</h1>
        <v-text-field dense label="用户名"></v-text-field>
        <v-text-field dense label="密码" type='password'></v-text-field>
        <v-btn color="warning" dark>登录</v-btn>
        <v-btn color="primary" @click="register" text>注册</v-btn>
    </div>
</template>

<script>
export default {
    methods: {
        register(){
            this.$router.push({name: "register"})
        }
    },
    
}
</script>


<style scoped>
    .singin{
        width: 500px;
        margin: 0 auto;
        text-align: center;
        }
</style>