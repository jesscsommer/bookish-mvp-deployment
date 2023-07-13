import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';

import { useFormik } from "formik";
import * as yup from "yup";
import Cookies from "js-cookie";

import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";

import { UserContext } from '../../context/userContext';

import Error from '../building_blocks/Error';

const EditProfileForm = () => {
    const navigate = useNavigate()
    const { user, dispatch : userDispatch } = useContext(UserContext)

    const [open, setOpen] = useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };
    
    const handleClose = () => {
        setOpen(false);
    };

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
        display_name: yup
        .string()
        .min(5, "Display name must be at least 5 characters")
        .max(50, "Display name must be at most 50 characters")
        .notRequired(),
        bio: yup
        .string()
        .max(250, "Bio must be at most 250 characters")
        .notRequired()
    });

    const formik = useFormik({
        initialValues: {
            username: user?.username,
            display_name: user?.display_name,
            email: user?.email,
            bio: user?.bio
        },
        validationSchema: userSchema,
        enableReinitialize: true,
        onSubmit: (values) => {
            // debugger
            (async () => {
                const res = await fetch(`../api/v1/users/${user.id}`, {
                    method: "PATCH",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(values)
                })
                if (res.ok) {
                    const updated_user = await res.json()
                    userDispatch({type: "fetch", payload: updated_user})
                    navigate(`/profile/${updated_user.username}`)
                } else {
                    const err = await res.json()
                    console.log(err)
                    // setErrors(err.error)
                }
            })();
        }
    })

    const handleDelete = () => {
        (async () => {
            const res = await fetch(`/api/v1/users/${user.id}`, { method : "DELETE" })
            if (res.ok) {
                userDispatch({ type: "fetch", payload: null })
                navigate("/")
            }
        })();
    }

    return (
        <div>
            <Button variant="outlined" onClick={handleClickOpen}>
                Edit profile
            </Button>
            <Dialog open={open} onClose={handleClose}>
                <DialogTitle>Edit profile</DialogTitle>
                <DialogContent>
                <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="username"
                        label="Username"
                        name="username"
                        autoComplete="username"
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        value={formik.values.username}
                    />
                    {formik.errors.username && formik.touched.username ? 
                        <Error severity="warning" error={formik.errors.username} /> 
                        : null}
                    <TextField
                        margin="normal"
                        fullWidth
                        id="display_name"
                        label="Display name"
                        name="display_name"
                        autoComplete="display_name"
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        value={formik.values.display_name || ""}
                    />
                    {formik.errors.display_name && formik.touched.display_name ? 
                        <Error severity="warning" error={formik.errors.display_name} /> 
                        : null}
                    { user?.google_unique_id ? 
                        null :
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
                            /> } 
                        {formik.errors.email && formik.touched.email ? 
                        <Error severity="warning" error={formik.errors.email} /> 
                        : null}
                    <TextField
                        margin="normal"
                        // required
                        fullWidth
                        multiline
                        id="bio"
                        label="Bio"
                        name="bio"
                        autoComplete="bio"
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                        value={formik.values.bio || ""}
                    />
                    {formik.errors.bio && formik.touched.bio ? 
                        <Error severity="warning" error={formik.errors.bio} /> 
                        : null}
                </DialogContent>
                <DialogActions>
                    {/* <Button onClick={handleClose}>Cancel</Button> */}
                    <Button
                        // sx={{ maxWidth: 1/8 }}
                        onClick={handleDelete}
                        variant="text">
                            Delete account
                    </Button>
                    <Button 
                        // sx={{ maxWidth: 1/3 }}
                        // justifyContent="center"
                        variant="contained"
                        onClick={() => {
                            formik.handleSubmit()
                            handleClose()
                        }}>
                            Update
                    </Button>
                </DialogActions>
            </Dialog>
    </div>
    )
}

export default EditProfileForm