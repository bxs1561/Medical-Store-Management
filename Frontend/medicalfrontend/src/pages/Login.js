import React, {useState} from "react";
import 'adminbsb-materialdesign/plugins/bootstrap/css/bootstrap.css'
import 'adminbsb-materialdesign/plugins/node-waves/waves.css'
import 'adminbsb-materialdesign/plugins/animate-css/animate.css'
import 'adminbsb-materialdesign/css/style.css'
import GoogleFontLoader from "react-google-font";
import login from "../utils/AuthHandler";


function Login(){
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [btnDisabled, setBtnDisabled] = useState(true);
    const [loginStatus, setLoginStatus] = useState(0);

    const formSubmit=(event)=>{
        event.preventDefault()
        login(username,password)

    }



    document.body.className="login-page";
    return(
        <>
            <GoogleFontLoader
                fonts={[
                    {
                        font: "Roboto",
                        weights: [400, 700],
                    },
                ]}
                subsets={["latin", "cyrillic-ext"]}
            />
            <GoogleFontLoader
                fonts={[
                    {
                        font: "Material+Icons",
                    },
                ]}
            />
        <div className="login-box">
            <div className="logo">
                <a>Medical Store Management System</a>
            </div>
            <div className="card">
                <div className="body">
                    <form id="sign_in" method="POST" onSubmit={formSubmit}>
                        <div className="msg">Sign in to start your session</div>
                        <div className="input-group">
                        <span className="input-group-addon">
                            <i className="material-icons">person</i>
                        </span>
                            <div className="form-line">
                                <input type="text" className="form-control" value={username} placeholder="Username"
                                       required autoFocus
                                       onChange={event => setUsername(event.target.value)}
                                />
                            </div>
                        </div>
                        <div className="input-group">
                        <span className="input-group-addon">
                            <i className="material-icons">lock</i>
                        </span>
                            <div className="form-line">
                                <input type="password"
                                       className="form-control"
                                       value={password}
                                       placeholder="Password"
                                       required
                                       onChange={event => setPassword(event.target.value)}/>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-xs-8 p-t-5">
                                <input type="checkbox" name="rememberme" id="rememberme"
                                       className="filled-in chk-col-pink"/>
                                    <label htmlFor="rememberme">Remember Me</label>
                            </div>
                            <div className="col-xs-4">
                                <button className="btn btn-block bg-pink waves-effect" type="submit"
                                >SIGN IN</button>
                            </div>
                        </div>
                        <div className="row m-t-15 m-b--20">
                            <div className="col-xs-6">
                                <a href="sign-up.html">Register Now!</a>
                            </div>
                            <div className="col-xs-6 align-right">
                                <a href="forgot-password.html">Forgot Password?</a>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
            </>
    )
} export default Login
