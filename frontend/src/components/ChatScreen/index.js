import React, {Component} from "react";
import SideBar from "./SideBar";
import Feed from "./Feed";

class ChatScreen extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            discussion: null,
            loaded: false,
            placeholder: "Loading"
        };
        this.displayFeed = this.displayFeed.bind(this)
    }

    componentDidMount() {
        fetch("/api/discussion")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return {placeholder: "Something went wrong!"};
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

    displayFeed(id) {
        fetch(`/api/discussion/${id}`).then(res => res.json()).then(data => {
            this.setState({discussion: data})
        }).catch(err => console.log(err))
    }

    render() {
        return (
            <section className="main-container">
                <h1 style={{display: "none"}}>Empty Heading</h1>
                <div>
                    <div id="frame">
                        {
                            this.state.loaded ?
                                <SideBar displayFeed={this.displayFeed} data={this.state.data}/>
                                : "Loading ..."
                        }
                        {
                            this.state.discussion && <Feed discussion={this.state.discussion}/>
                        }
                    </div>
                </div>


                <footer className="footer-container">
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-md-12 col-sm-12">
                                <div className="float-left">
                                    © 2021 Bird&nbsp;&nbsp;&nbsp;&bull;&nbsp;&nbsp;&nbsp; InfluenceMe <a
                                    href="http://influenceme.com"
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