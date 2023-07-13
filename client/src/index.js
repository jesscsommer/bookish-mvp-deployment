import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./components/App";
import { BookProvider } from "./context/bookContext"
import { BookShelfProvider } from "./context/bookShelfContext"
import { ShelfProvider } from "./context/shelfContext"
import { ErrorProvider } from "./context/errorContext"
import { UserProvider } from "./context/userContext";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
    <UserProvider>
        <ErrorProvider>
            <BookProvider>
                <ShelfProvider>
                    <BookShelfProvider>
                            <BrowserRouter>
                                <App />
                            </BrowserRouter>
                    </BookShelfProvider>
                </ShelfProvider>
            </BookProvider>
        </ErrorProvider>
    </UserProvider>
);