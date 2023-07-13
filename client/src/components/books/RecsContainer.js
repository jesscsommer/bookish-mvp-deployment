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
import BookCard from './BookCard';

const defaultTheme = createTheme()

const RecsContainer = ({ recs }) => {
    return (
        <ThemeProvider theme={defaultTheme}>
        <CssBaseline />
            <main>
            <Container sx={{ py: 8 }} maxWidth="md">
                <Grid container spacing={4}>
                {recs?.map(rec => <BookCard book={rec} key={rec.id} />)}
                </Grid>
            </Container>
            </main>
        </ThemeProvider>
    )
}

export default RecsContainer