import axios from './http'

const user = {
    singin(param){
        return axios.post("/singin", param)
    },
    register(param){
        return axios.post("/register", param)
    },
}
export default user