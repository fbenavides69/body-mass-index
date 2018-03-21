jest.dontMock('../js/index')

import React from 'react';
import { configure, shallow, mount } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

import BmiReactForm from '../js/App';

configure({ adapter: new Adapter() });

describe('Renders Form', () => {

    it('Renders Height', () => {
        const wrapper = shallow(<BmiReactForm />);

        expect(wrapper.findWhere(n => n.type() === 'label' && n.contains('Height')))
    });

    it('Renders Weight', () => {
        const wrapper = shallow(<BmiReactForm />);

        expect(wrapper.findWhere(n => n.type() === 'label' && n.contains('Weight')))
    });

    it('Renders Factor', () => {
        const wrapper = shallow(<BmiReactForm />);

        expect(wrapper.findWhere(n => n.type() === 'label' && n.contains('Factor')))
    });

    it('Renders Category', () => {
        const wrapper = shallow(<BmiReactForm />);

        expect(wrapper.findWhere(n => n.type() === 'label' && n.contains('Category')))
    });

});
