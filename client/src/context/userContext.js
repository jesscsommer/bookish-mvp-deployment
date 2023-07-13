import { useEffect, useReducer, createContext } from "react";
import Cookie from "js-cookie";

const UserContext = createContext()

const initialState = null

const reducer = (state, action) => {
    switch (action.type) {
        case "fetch":
            return action.payload
        case "remove":
            return initialState
        default:
            return state;
    }
}

const UserProvider = ({ children }) => {
    const [user, dispatch] = useReducer(reducer, initialState)

    useEffect(() => {
        (async () => {
            const res = await fetch("/me")
            // debugger
            if (res.ok) {
                const data = await res.json()
                dispatch({ type: "fetch", payload: data.user })
            } 
        })();
    }, [])

    return (
        <UserContext.Provider value={{ user, dispatch }}>
            { children }
        </UserContext.Provider>
    )
}

export { UserContext, UserProvider }