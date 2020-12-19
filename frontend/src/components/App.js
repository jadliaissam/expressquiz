import React, {Component} from "react";
import {render} from "react-dom";
import ChatScreen from './ChatScreen'

class App extends Component {
    render() {
        return (
            <ChatScreen/>
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App/>, container);