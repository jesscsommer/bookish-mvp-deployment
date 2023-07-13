import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';

const DeleteButton = ({ handleClick }) => {
    return (
        <IconButton onClick={handleClick} aria-label="delete">
            <DeleteIcon />
        </IconButton>
    )
}

export default DeleteButton