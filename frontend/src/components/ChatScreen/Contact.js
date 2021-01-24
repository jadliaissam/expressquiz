import React from "react";

function Contact(props) {
    return <li className="contact">
        <div className="wrap" onClick={props.onClick}>
            <span className="contact-status online"/>
            <img src="http://via.placeholder.com/80x80" alt=""/>
            <div className="meta">
                <p className="name">{props.d.users[1].first_name + " " + props.d.users[1].last_name}</p>
                <p className="preview">{props.d.messages[0].content}</p>
            </div>
        </div>
    </li>;
}

export default Contact;