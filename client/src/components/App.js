import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import AddShelfForm from "./shelves/AddShelfForm";
import AuthForm from "./account/AuthForm";
import BookCard from "./books/BookCard";
import BooksContainer from "./books/BooksContainer";
import BookDetail from "./books/BookDetail";
import Buttons from "./building_blocks/Buttons";
import DeleteButton from "./building_blocks/DeleteButton";
import EditButton from "./building_blocks/EditButton";
import EditProfileForm from "./account/EditProfileForm";
import Error from "./building_blocks/Error";
import Header from "./building_blocks/Header";
import Profile from "./account/Profile";
import Shelf from "./shelves/Shelf";
import ShelfContainer from "./shelves/ShelfContainer";
import NotFound from "./building_blocks/NotFound";

import { useContext } from "react";
import { UserContext } from "../context/userContext";

const App = () => {
    const { user } = useContext(UserContext)

    return (
        <div className="app">
        <Header />
        <Routes>
            <Route 
            path="/login" 
            element={
                <AuthForm />
            }/>
            <Route 
                path="/shelves" 
                element={
                    <ShelfContainer />
                }/>
            <Route 
                path="/profile/:username" 
                element={
                <Profile />
            }/>
            <Route 
                path="/books/:id" 
                element={
                    <BookDetail />
                }/>
            <Route 
                path="/" 
                element={
                    <BooksContainer />
                }/>
            <Route 
                path="*" 
                element={
                    <NotFound />
                }/>
        </Routes>
        </div>
    )
}

export default App
