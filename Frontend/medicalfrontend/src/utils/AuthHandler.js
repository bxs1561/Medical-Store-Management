import axios from 'axios'
function login(username,password) {
        let user = {
            username: username,
            password: password
        }
        axios.post('http://localhost:8000/api/gettoken/',user).then(response=>{
            localStorage.setItem("token",response.data.access)
            localStorage.setItem("refresh",response.data.refresh)

            }
        ).catch(err=>{
            console.log(err)
        })



}export default login
