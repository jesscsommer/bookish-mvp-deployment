import { useReducer, createContext } from "react"

const ErrorContext = createContext()

const initialState = null

const reducer = (state, action) => {
    switch (action.type) {
        case "add":
            return [action.payload, ...state]
        case "remove":
            return initialState
        default:
            return state;
    }
}

const ErrorProvider = ({ children }) => {
    const [errors, dispatch] = useReducer(reducer, initialState)

    return (
        <ErrorContext.Provider value={{ errors, dispatch }}>
            { children }
        </ErrorContext.Provider>
    )
}

export { ErrorContext, ErrorProvider }