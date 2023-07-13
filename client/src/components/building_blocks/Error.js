import Alert from '@mui/material/Alert';

const Error = ({ severity, error }) => {
    return (
        <Alert severity={severity}>{error}</Alert>
    )
}

export default Error