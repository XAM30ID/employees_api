// context/UsersContext.js
import React, { createContext, useState, useContext, useCallback } from 'react';
import { api } from '../api/api';

const UsersContext = createContext();

export const UsersProvider = ({ children }) => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [user, setUser] = useState(null);

  const fetchUsers = useCallback(async (fullname='') => {
    setLoading(true);
    try {
      const response = await api.get('http://127.0.0.1:8000/users?name_filter=' + fullname);
      setUsers(response.data.users);
    } catch (error) {
      console.error('Ошибка:', error);
    } finally {
      setLoading(false);
    }
  }, []);

  const value = {
    users,
    loading,
    fetchUsers,
    setUser,
    user
  };

  return (
    <UsersContext.Provider value={value}>
      {children}
    </UsersContext.Provider>
  );
};

export const useUsersContext = () => {
  const context = useContext(UsersContext);
  if (!context) {
    throw new Error('useUsersContext must be used within UsersProvider');
  }
  return context;
};