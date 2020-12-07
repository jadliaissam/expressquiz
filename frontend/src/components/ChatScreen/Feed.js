import React from "react"

const Feed = (props) => {
    const fullname = `${props.discussion.users[1].first_name} ${props.discussion.users[1].last_name}`
    return (
        <div className="content">
            <div className="contact-profile">
                <img src="http://via.placeholder.com/80x80" alt=""/>
                <p>{fullname}</p>
                <div className="social-media">
                    <i className="icon-facebook" aria-hidden="true"/>
                    <i className="icon-twitter" aria-hidden="true"/>
                    <i className="icon-instagram" aria-hidden="true"/>
                </div>
            </div>
            <div className="messages">
                <ul>
                    {props.discussion.messages.map(msg => <li
                            className={msg.message_sender === 18 ? "sent" : "replies"}>
                            <img src="http://via.placeholder.com/80x80" alt=""/>
                            <p>{msg.content}</p>
                        </li>
                    )}

                    <li className="replies">
                        <img src="http://via.placeholder.com/80x80" alt=""/>
                        <p>When you're backed against the wall, break the god damn thing down.</p>
                    </li>
                </ul>
            </div>
            <div className="message-input">
                <div className="wrap">
                    <input type="text" placeholder="Write your message..."/>
                    <i className="icon-attachment attachment" aria-hidden="true"/>
                    <button className="submit"><i className="icon-paperplane" aria-hidden="true"/>
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Feed;