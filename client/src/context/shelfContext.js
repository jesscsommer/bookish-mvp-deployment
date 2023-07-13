import { useEffect, useReducer, createContext } from "react"

const ShelfContext = createContext()

const initialState = []

const reducer = (state, action) => {
    switch (action.type) {
        case "fetch":
            return action.payload
        case "add":
            return [action.payload, ...state]
        case "patch":
            return state.map(shelf => shelf.id === action.payload.id ? 
                            action.payload : shelf)
        case "remove":
            return state.filter(shelf => shelf.id !== action.payload)
        case "reset":
            return initialState
        default:
            return state;
    }
}

const ShelfProvider = ({ children }) => {
    const [shelves, dispatch] = useReducer(reducer, initialState)

    useEffect(() => {
        (async () => {
            const res = await fetch("/me")
            // debugger
            if (res.ok) {
                const data = await res.json()
                dispatch({ type: "fetch", payload: data.user?.shelves })
            } 
        })();
    }, [])

    return (
        <ShelfContext.Provider value={{ shelves, dispatch }}>
            { children }
        </ShelfContext.Provider>
    )
}

export { ShelfContext, ShelfProvider }