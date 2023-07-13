import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import IconButton from "@mui/material/IconButton";
import InputAdornment from "@mui/material/InputAdornment";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";

import { useState, useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";

import { useFormik } from "formik";
import * as yup from "yup";

import Error from '../building_blocks/Error';
import { UserContext } from '../../context/userContext';

const defaultTheme = createTheme();

const AuthForm = () => {
    const navigate = useNavigate()
    const { user, dispatch : userDispatch } = useContext(UserContext)

    const [ isLogin, setIsLogin ] = useState(true)

    const [showPassword, setShowPassword] = useState(false)
    const handleClickShowPassword = () => setShowPassword((show) => !show);

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    const [ errors, setErrors ] = useState(null)

    const userSchema = yup.object().shape({
        username: yup
        .string()
        .min(5, "Username must be at least 5 characters")
        .max(20, "Username must be at most 20 characters")
        .test(
            "valid-chs",
            "Username may only contain letters and numbers",
            (value) => {
                return /^[A-z0-9]+$/.test(value);
            }
        )
        .required("Username is required"),
        email: yup
        .string()
        .test(
            "valid-email",
            "Email must be valid",
            (value) => {
                return /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|'(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*')@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/.test(value)
            }
        )
        .required("Email is required"),
        password: yup
        .string()
        .test(
            "valid-pw", 
            "Password must include at least 1 uppercase letter, 1 number, and 1 symbol",
            (value) => {
                return /[A-Z]/.test(value) && /[0-9]/.test(value) && /[!@#$%^&*]/.test(value);
            }
        )
        .min(10, "Password must be at least 10 characters")
        .required("Password is required"),
    });

    const formik = useFormik({
        initialValues: {
            username: "",
            email: "",
            password: ""
        },
        validationSchema: isLogin ? null : userSchema,
        onSubmit: (values) => {
            (async () => {
                const endpoint = isLogin ? "/login" : "/signup"
                const res = await fetch(endpoint, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(values)
                })
                if (res.ok) {
                    const new_user = await res.json()
                    userDispatch({type: "fetch", payload: new_user.user })
                    isLogin ? navigate("/") : navigate(`/profile/${new_user.user.username}`)
                } else {
                    const err = await res.json()
                    setErrors(err.error)
                }
            })();
        }
    })

    // const handleLoginWithGoogle = () => {
    //     (async () => {
    //         const res = await fetch("/login_with_google", {
    //             method: "POST",
    //             headers: {
    //                 "Access-Control-Allow-Origin": "*",
    //                 "Access-Control-Allow-Headers": "Content-Type",
    //             },
    //             // mode: "no-cors"
    //         })
    //     })();
    // }

    return (
        <ThemeProvider theme={defaultTheme}>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box
                    sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    }}
                >
                    <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    </Avatar>
                    <Typography component="h1" variant="h5">
                    {isLogin ? "Log in" : "Sign up"}
                    </Typography>
                    <Box 
                        component="form" 
                        onSubmit={formik.handleSubmit} 
                        noValidate sx={{ mt: 1 }}
                        >
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="username"
                        label="Username"
                        name="username"
                        autoComplete="username"
                        autoFocus
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        value={formik.values.username}
                    />
                    {formik.errors.username && formik.touched.username ? 
                        <Error severity="warning" error={formik.errors.username} /> 
                        : null}
                    {isLogin ? null :
                        <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.email}
                            // autoFocus
                        />}
                        {formik.errors.email && formik.touched.email ? 
                        <Error severity="warning" error={formik.errors.email} /> 
                        : null}
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        id="password"
                        autoComplete="current-password"
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        value={formik.values.password}
                        type={showPassword ? "text" : "password"}
                        InputProps={{
                            endAdornment: (
                            <InputAdornment position="end">
                                <IconButton
                                aria-label="toggle password visibility"
                                onClick={handleClickShowPassword}
                                onMouseDown={handleMouseDownPassword}
                                >
                                {showPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                            ),
                        }}
                    />
                    {formik.errors.password && formik.touched.password ? 
                        <Error severity="warning" error={formik.errors.password} /> 
                        : null}
                    {errors ? <Error severity="error" error={errors} /> : null}
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        {isLogin ? "Log in" : "Sign up"}
                    </Button>
                    <Link
                        href="/login_with_google">
                        <Button
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            Login with Google
                        </Button>
                    </Link>
                    <Grid container>
                        <Grid item>
                        <Link 
                            onClick={() => {
                                setIsLogin(isLogin => !isLogin)
                                setErrors(null)
                            }} 
                            variant="body2">
                            {isLogin ? "Don't have an account? Sign Up" : "Already have an account? Log in"}
                        </Link>
                        </Grid>
                    </Grid>
                    </Box>
                </Box>
            </Container>
        </ThemeProvider>
    )
}

export default AuthForm