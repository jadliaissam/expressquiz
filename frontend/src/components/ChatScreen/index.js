import React, { Component } from "react";
import SideBar from "./SideBar";

class ChatScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
        <section className="main-container">
          <h1 style={{display:'none'}}>Empty Heading</h1>

          <div>
            <div id="frame">
              <SideBar />
              <div className="content">
                <div className="contact-profile">
                  <img src="http://via.placeholder.com/80x80" alt=""/>
                  <p>Jacqueline Howell</p>
                  <div className="social-media">
                    <i className="icon-facebook" aria-hidden="true"></i>
                    <i className="icon-twitter" aria-hidden="true"></i>
                    <i className="icon-instagram" aria-hidden="true"></i>
                  </div>
                </div>
                <div className="messages">
                  <ul>
                    <li className="sent">
                      <img src="http://via.placeholder.com/80x80" alt=""/>
                      <p>How the hell am I supposed to get a jury to believe you when I am not even sure that I do?!</p>
                    </li>
                    <li className="replies">
                      <img src="http://via.placeholder.com/80x80" alt=""/>
                      <p>When you're backed against the wall, break the god damn thing down.</p>
                    </li>
                  </ul>
                </div>
                <div className="message-input">
                  <div className="wrap">
                    <input type="text" placeholder="Write your message..."/>
                    <i className="icon-attachment attachment" aria-hidden="true"></i>
                    <button className="submit"><i className="icon-paperplane" aria-hidden="true"></i></button>
                  </div>
                </div>
              </div>
            </div>

          </div>


          <footer className="footer-container">
            <div className="container-fluid">
              <div className="row">
                <div className="col-md-12 col-sm-12">
                  <div className="float-left">
                    © 2021 Bird&nbsp;&nbsp;&nbsp;&bull;&nbsp;&nbsp;&nbsp; InfluenceMe <a href="http://influenceme.com"
                                                                                         target="_blank">InfluenceMe</a>.
                  </div>
                  <div className="float-right">
                    <div className="badge badge-danger">Version: 0.0.1</div>
                  </div>
                </div>
              </div>
            </div>
          </footer>
        </section>
    );
  }
}

export default ChatScreen;