// src/contexts/UserContext.tsx
import React, {
    createContext,
    useContext,
    useState,
    useEffect,
    ReactNode,
  } from "react";
  import {
    getAuth,
    onAuthStateChanged,
    User as FirebaseUser,
  } from "firebase/auth";
  
  // Define la interfaz para el contexto de usuario
  interface UserContextProps {
    user: FirebaseUser | null;
  }
  
  // Crea el contexto de usuario
  const UserContext = createContext<UserContextProps | undefined>(undefined);
  
  // Hook personalizado para usar el contexto de usuario
  export const useUser = (): FirebaseUser | null => {
    const context = useContext(UserContext);
    if (!context) {
      throw new Error("useUser debe ser usado dentro de un UserProvider");
    }
    return context.user;
  };
  
  // Define las propiedades del proveedor de usuario
  interface UserProviderProps {
    children: ReactNode;
  }
  
  // Proveedor de usuario que envuelve la aplicación y proporciona el estado del usuario
  export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
    const [user, setUser] = useState<FirebaseUser | null>(null);
    const auth = getAuth();
  
    useEffect(() => {
      const unsubscribe = onAuthStateChanged(auth, (user) => {
        setUser(user);
      });
      return () => unsubscribe();
    }, [auth]);
  
    return (
      <UserContext.Provider value={{ user }}>{children}</UserContext.Provider>
    );
  };
  