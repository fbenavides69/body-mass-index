// index.jsx
import React from "react";
import ReactDOM from "react-dom";

class BmiReactForm extends React.Component {

    constructor(props) {

        super(props);
        this.state = { 
            height: 0,
            weight: 0,
            factor: 'Unknown',
            category: 'Undefined'
        };

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(input, value) {

        this.setState({[input]: value});

        const height = parseFloat(this.state.height).toFixed(2);
        const weight = parseFloat(this.state.weight).toFixed(2);
        this.bmiCalc(height, weight);
    }

    bmiCalc(height, weight) {

        if ((height > 0) && (weight > 0)) {

            let bmiNumber = weight/(height * height);

            let bmiString = 'Undefined'
            switch(true) {
                case (bmiNumber < 15):
                    bmiString = 'Very severely underweight';
                    break;
                case (bmiNumber >= 15 && bmiNumber < 16):
                    bmiString = 'Severely underweight';
                    break;
                case (bmiNumber >= 16 && bmiNumber < 18.5):
                    bmiString = 'Underweight';
                    break;
                case (bmiNumber >= 18.5 && bmiNumber < 25):
                    bmiString = 'Normal (healthy weight)';
                    break;
                case (bmiNumber >= 25 && bmiNumber < 30):
                    bmiString = 'Overweight';
                    break;
                case (bmiNumber >= 30 && bmiNumber < 35):
                    bmiString = 'Obese Class I (Moderately obese)';
                    break;
                case (bmiNumber >= 35 && bmiNumber < 40):
                    bmiString = 'Obese Class II (Severely obese)';
                    break;
                case (bmiNumber >= 40):
                    bmiString = 'Obese Class III (Very severely obese)';
                    break;
            }

            this.setState({factor: bmiNumber});
            this.setState({category: bmiString});

        } else {

            this.setState({factor: 'Unknown'});
            this.setState({category: 'Undefined'});
        }
    }

    render() {

        const factor = this.state.factor;
        const category = this.state.category;

        return (
            <div>
                <form>
                    <input id="csrf_token" name="csrf_token" type="hidden" value="IjFhOWU1NTg2OWFiYTA0NTMzYjhhMDM5YWRhOGNjOThhMTk1MDJiNjEi.DYtlyQ.k8gVqs8uX9TLTOrnTF3aeOJXjoY" />
                    <p>
                        <label>Height</label> <input class="form-control"
                            id="height" type="text"
                            name="height"
                            placeholder={this.state.height}
                            onChange={e => this.handleChange('height', e.target.value)} />
                    </p>
                    <p>
                        <label>Weight</label> <input class="form-control"
                            id="weight" type="text"
                            name="weight"
                            placeholder={this.state.weight}
                            onChange={e => this.handleChange('weight', e.target.value)} />
                    </p>
                    <div class="jumbotron">
                        <p>
                            <label>Factor:</label> <span>{factor}</span>
                        </p>
                        <p>
                            <label>Category:</label> <span>{category}</span>
                        </p>
                    </div>
                </form>
            </div>
        );
    }
}

ReactDOM.render(<BmiReactForm />, document.getElementById("BmiReactForm"));
