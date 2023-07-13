import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { v4 as uuid } from "uuid";

import BookCard from '../books/BookCard';
import DeleteButton from "../building_blocks/DeleteButton"
import { UserContext } from '../../context/userContext';
import { useContext } from 'react';
import { BookShelfContext } from '../../context/bookShelfContext';

const defaultTheme = createTheme()

const cards = [1, 2, 3];

const Shelf = ({ shelf }) => {
    const { user, dispatch : userDispatch } = useContext(UserContext)
    const { bookShelves, dispatch : bookShelfDispatch } = useContext(BookShelfContext)

    // console.log("This is the shelf")
    // console.log

    // console.log(shelf.books)

    // const handleClick = (shelf_id) => {
    //     (async () => {
    //         const res = await fetch(`/shelves/${shelf_id}`, { method: "DELETE" })
    //         if (res.ok){
    //             userDispatch({ type: "fetch", payload: { ...user }})
    //         }
    //     })();
    // }

    return (
        <Grid container mt={2} spacing={4}>
            <Box sx={{ width: 1 }}>
                <Typography variant="h5">
                    {shelf?.name}
                    {/* <DeleteButton handleClick={() => handleClick(shelf.id)} /> */}
                </Typography>
            </Box>
            {shelf?.books?.map((book) => (
                <BookCard key={uuid()} book={book} shelf={shelf}/>
            ))}
        </Grid>
    )
}

export default Shelf