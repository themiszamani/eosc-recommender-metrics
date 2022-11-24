import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Mesure impact of Recommender System',
    Svg: require('@site/static/img/undraw_visionary_technology_re_jfp7.svg').default,
    description: (
      <>
        Measure the impact of the AI-enhanced services powering the EOSC Marketplace
      </>
    ),
  },
  {
    title: 'Analyse and Evaluate',
    Svg: require('@site/static/img/undraw_data_processing_yrrv.svg').default,
    description: (
      <>
        Evaluate and compute RS related metrics & KPIs
      </>
    ),
  },
  {
    title: 'Generate Reports',
    Svg: require('@site/static/img/undraw_analytics_re_dkf8.svg').default,
    description: (
      <>
        Generate Rich reports with results and graphs
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
