import React from "react";
import "../styles/Landing.css";
// import FadeInSection from "./FadeInSection"; 

class Landing extends React.Component {
    constructor() {
        super();
        this.state = {
            expanded: true,
            activeKey: "1"
        };
        this.handleSelect = this.handleSelect.bind(this);
    }
    handleSelect(eventKey) {
        this.setState({
            activeKey: eventKey
        });
    }
    render() {
        const one = (
            <h1>
                Let's find the best articles for your needs.
            </h1>
        );
        const two = (
            <p>
                Get started by answering a few short questions.
            </p>
        );
        const three = (
            // Button goes here
        );

        return (
            <div id="Landing">
                // <FadeInSection>
                    <div className="section-header">
                        <span className="section-title">
                            {[one]}
                        </span>
                    </div>
                    <div className="landing-content">
                        <div className="about-description">
                            {[two]}
                            {[three]}
                        </div>
                    </div>
               // </FadeInSection>
            </div>
        )
    }
}


export default Landing;