import React from "react";
import Contact from './Contact'

const SideBar = (props) => {
    return (
        <div id="sidepanel">
            <div id="profile">
                <div className="wrap">
                    <img id="profile-img" src="http://via.placeholder.com/80x80" className="online" alt=""/>
                    <p>Jane Elliott</p>
                    <i className="icon-arrow-down32 expand-button" aria-hidden="true"/>
                    <div id="status-options">
                        <ul>
                            <li id="status-online" className="active"><span className="status-circle"/>
                                <p>Online</p>
                            </li>
                            <li id="status-away"><span className="status-circle"/> <p>Away</p></li>
                            <li id="status-busy"><span className="status-circle"/> <p>Busy</p></li>
                            <li id="status-offline"><span className="status-circle"/> <p>Offline</p></li>
                        </ul>
                    </div>
                    <div id="expanded">
                        <label><i className="icon-facebook" aria-hidden="true"/></label>
                        <input name="twitter" type="text" value="facebook"/>
                        <label><i className="icon-twitter" aria-hidden="true"/></label>
                        <input name="twitter" type="text" value="twitter"/>
                        <label><i className="icon-instagram" aria-hidden="true"/></label>
                        <input name="twitter" type="text" value="instagram"/>
                    </div>
                </div>
            </div>
            <div id="search">
                <label><i className="icon-search4" aria-hidden="true"/></label>
                <input type="text" placeholder="Search contacts..."/>
            </div>
            <div id="contacts">
                <ul>
                    {[1, 2, 3, 4, 5, 6].map(e => <Contact/>)}
                    <li className="contact active">
                        <div className="wrap">
                            <span className="contact-status busy"/>
                            <img src="http://via.placeholder.com/80x80" alt=""/>
                            <div className="meta">
                                <p className="name">Jacqueline Howell</p>
                                <p className="preview">Wrong. You take the gun, or you pull out a bigger one. Or, you
                                    call
                                    their bluff. Or, you do any one of a hundred and forty six other things.</p>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div id="bottom-bar">
                <button id="addcontact"><i className="icon-user-plus" aria-hidden="true"/> <span>Add contact</span>
                </button>
                <button id="setting"><i className="icon-gear" aria-hidden="true"/> <span>Settings</span></button>
            </div>
        </div>

    )
}

export default SideBar;