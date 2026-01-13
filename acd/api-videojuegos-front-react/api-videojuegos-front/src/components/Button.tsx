import React, { Children } from "react";
import '../styles/components/Button.css'; // Assuming you have a CSS file for styling

export const Button = ({ onClick, value, className, id }: { onClick: () => void; value: React.ReactNode; className?: string; id?: string }) => {
    return (
        <a onClick={onClick} id={id} className={className} >
            {value}
        </a>
    );
};