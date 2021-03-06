import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import './reset.min.css';
import "bootstrap/dist/css/bootstrap.css";
import './index.css';
import { Application } from './App';
import { Provider } from 'react-redux';
import { store } from './reducers/index';
// import registerServiceWorker from './registerServiceWorker';

// import { getToken } from './config/adalConfig';

ReactDOM.render(
    <Provider store={store}>
        <BrowserRouter>
            <Application />
        </BrowserRouter>
    </Provider>,
    document.getElementById('root')
);
// registerServiceWorker();
