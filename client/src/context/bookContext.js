import { useEffect, useReducer, createContext } from "react"

const BookContext = createContext()

const initialState = []

const reducer = (state, action) => {
    switch (action.type) {
        case "fetch":
            return action.payload
        case "add":
            return [action.payload, ...state]
        case "patch":
            return state.map(book => book.id === action.payload.id ? 
                            action.payload : book)
        case "remove":
            return state.filter(book => book.id !== action.payload.id)
        default:
            return state;
    }
}

const BookProvider = ({ children }) => {
    const [books, dispatch] = useReducer(reducer, initialState)

    useEffect(() => {
        (async () => {
            const res = await fetch("/api/v1/books")
            if (res.ok) {
                const books = await res.json()
                dispatch({ type: "fetch", payload: books })
            } else {
                // add error handling
            }
        })();
    }, [])

    return (
        <BookContext.Provider value={{ books, dispatch }}>
            { children }
        </BookContext.Provider>
    )
}

export { BookContext, BookProvider }