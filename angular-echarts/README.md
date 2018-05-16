# AngularEcharts

This project is used to show how to integrate Angular with ECharts. The application framework is generate with [Angular CLI](https://github.com/angular/angular-cli) version 1.7.4.

The following is the stemps to add in ECharts module:
1. Install ECharts by running: npm install echarts --save
2. Modify .angular-cli.json file to include echarts scripts
      "scripts": [
        "../node_modules/echarts/dist/echarts.min.js"
      ],
3. Modify typings.d.ts file to include echarts declaration

    declare var echarts: any;

4. Now you can use echarts. Refere to the contents in app.components.ts for how the chart is created and how to set chart options

5. Create a div section in app.components.html. Please note the id of the section must be same as the chart parameter in app.components.ts

6. To use echarts 3D extension, install echarts-gl by running: 
    npm install echarts-gl --save

    To make echarts-gl 1.1.0 work with echarts, the echarts version has to be 4.0.4. There are some errors when using echarts 4.1.0



## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
