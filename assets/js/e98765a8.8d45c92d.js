"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[787],{3905:(a,e,t)=>{t.d(e,{Zo:()=>l,kt:()=>k});var m=t(7294);function n(a,e,t){return e in a?Object.defineProperty(a,e,{value:t,enumerable:!0,configurable:!0,writable:!0}):a[e]=t,a}function r(a,e){var t=Object.keys(a);if(Object.getOwnPropertySymbols){var m=Object.getOwnPropertySymbols(a);e&&(m=m.filter((function(e){return Object.getOwnPropertyDescriptor(a,e).enumerable}))),t.push.apply(t,m)}return t}function s(a){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?r(Object(t),!0).forEach((function(e){n(a,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(a,Object.getOwnPropertyDescriptors(t)):r(Object(t)).forEach((function(e){Object.defineProperty(a,e,Object.getOwnPropertyDescriptor(t,e))}))}return a}function p(a,e){if(null==a)return{};var t,m,n=function(a,e){if(null==a)return{};var t,m,n={},r=Object.keys(a);for(m=0;m<r.length;m++)t=r[m],e.indexOf(t)>=0||(n[t]=a[t]);return n}(a,e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(a);for(m=0;m<r.length;m++)t=r[m],e.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(a,t)&&(n[t]=a[t])}return n}var i=m.createContext({}),o=function(a){var e=m.useContext(i),t=e;return a&&(t="function"==typeof a?a(e):s(s({},e),a)),t},l=function(a){var e=o(a.components);return m.createElement(i.Provider,{value:e},a.children)},c={inlineCode:"code",wrapper:function(a){var e=a.children;return m.createElement(m.Fragment,{},e)}},N=m.forwardRef((function(a,e){var t=a.components,n=a.mdxType,r=a.originalType,i=a.parentName,l=p(a,["components","mdxType","originalType","parentName"]),N=o(t),k=n,h=N["".concat(i,".").concat(k)]||N[k]||c[k]||r;return t?m.createElement(h,s(s({ref:e},l),{},{components:t})):m.createElement(h,s({ref:e},l))}));function k(a,e){var t=arguments,n=e&&e.mdxType;if("string"==typeof a||n){var r=t.length,s=new Array(r);s[0]=N;var p={};for(var i in e)hasOwnProperty.call(e,i)&&(p[i]=e[i]);p.originalType=a,p.mdxType="string"==typeof a?a:n,s[1]=p;for(var o=2;o<r;o++)s[o]=t[o];return m.createElement.apply(null,s)}return m.createElement.apply(null,t)}N.displayName="MDXCreateElement"},8478:(a,e,t)=>{t.r(e),t.d(e,{assets:()=>i,contentTitle:()=>s,default:()=>c,frontMatter:()=>r,metadata:()=>p,toc:()=>o});var m=t(7462),n=(t(7294),t(3905));const r={id:"accuracy",title:"Accuracy",sidebar_position:1},s="Accuracy",p={unversionedId:"metrics_descriptions/accuracy",id:"metrics_descriptions/accuracy",title:"Accuracy",description:"Summary",source:"@site/docs/metrics_descriptions/accuracy.md",sourceDirName:"metrics_descriptions",slug:"/metrics_descriptions/accuracy",permalink:"/eosc-recommender-metrics/docs/metrics_descriptions/accuracy",draft:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{id:"accuracy",title:"Accuracy",sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Metrics Descriptions",permalink:"/eosc-recommender-metrics/docs/category/metrics-descriptions"},next:{title:"Catalog Coverage",permalink:"/eosc-recommender-metrics/docs/metrics_descriptions/catalog_coverage"}},i={},o=[{value:"Summary",id:"summary",level:2},{value:"Description",id:"description",level:2},{value:"Output",id:"output",level:2},{value:"Prerequisites:",id:"prerequisites",level:2},{value:"Process Flow:",id:"process-flow",level:2}],l={toc:o};function c(a){let{components:e,...t}=a;return(0,n.kt)("wrapper",(0,m.Z)({},l,t,{components:e,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"accuracy"},"Accuracy"),(0,n.kt)("h2",{id:"summary"},"Summary"),(0,n.kt)("p",null,"Measures Recommendations' accuracy based on users' access to the services. A value of 1, indicates that the RS model got all the predictions right, and a value of 0 indicates that the RS model did not make a single correct prediction"),(0,n.kt)("h2",{id:"description"},"Description"),(0,n.kt)("p",null,"The accuracy ",(0,n.kt)("span",{parentName:"p",className:"math math-inline"},(0,n.kt)("span",{parentName:"span",className:"katex"},(0,n.kt)("span",{parentName:"span",className:"katex-mathml"},(0,n.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,n.kt)("semantics",{parentName:"math"},(0,n.kt)("mrow",{parentName:"semantics"},(0,n.kt)("mo",{parentName:"mrow",stretchy:"false"},"("),(0,n.kt)("mi",{parentName:"mrow"},"A")),(0,n.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"(A")))),(0,n.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,n.kt)("span",{parentName:"span",className:"base"},(0,n.kt)("span",{parentName:"span",className:"strut",style:{height:"1em",verticalAlign:"-0.25em"}}),(0,n.kt)("span",{parentName:"span",className:"mopen"},"("),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal"},"A")))))," of the recommendations is based on users' access to the services. A value of 1, indicates that the RS model got all the predictions right, and a value of 0 indicates that the RS model did not make a single correct prediction. Generally, the Accuracy mathematical expression is defined as:\n",(0,n.kt)("span",{parentName:"p",className:"math math-inline"},(0,n.kt)("span",{parentName:"span",className:"katex"},(0,n.kt)("span",{parentName:"span",className:"katex-mathml"},(0,n.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,n.kt)("semantics",{parentName:"math"},(0,n.kt)("mrow",{parentName:"semantics"},(0,n.kt)("mi",{parentName:"mrow"},"A"),(0,n.kt)("mo",{parentName:"mrow"},"="),(0,n.kt)("mfrac",{parentName:"mrow"},(0,n.kt)("mrow",{parentName:"mfrac"},(0,n.kt)("mi",{parentName:"mrow"},"N"),(0,n.kt)("mi",{parentName:"mrow"},"u"),(0,n.kt)("mi",{parentName:"mrow"},"m"),(0,n.kt)("mi",{parentName:"mrow"},"b"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"f"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"t"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"p"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"d"),(0,n.kt)("mi",{parentName:"mrow"},"i"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"t"),(0,n.kt)("mi",{parentName:"mrow"},"i"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"n"),(0,n.kt)("mi",{parentName:"mrow"},"s")),(0,n.kt)("mrow",{parentName:"mfrac"},(0,n.kt)("mi",{parentName:"mrow"},"T"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"t"),(0,n.kt)("mi",{parentName:"mrow"},"a"),(0,n.kt)("mi",{parentName:"mrow"},"l"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"n"),(0,n.kt)("mi",{parentName:"mrow"},"u"),(0,n.kt)("mi",{parentName:"mrow"},"m"),(0,n.kt)("mi",{parentName:"mrow"},"b"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"f"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"p"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"d"),(0,n.kt)("mi",{parentName:"mrow"},"i"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"t"),(0,n.kt)("mi",{parentName:"mrow"},"i"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"n"),(0,n.kt)("mi",{parentName:"mrow"},"s")))),(0,n.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"A=\\frac{Number\\;of\\;correct\\;predictions}{Total\\;number\\;of\\;predictions}")))),(0,n.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,n.kt)("span",{parentName:"span",className:"base"},(0,n.kt)("span",{parentName:"span",className:"strut",style:{height:"0.6833em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal"},"A"),(0,n.kt)("span",{parentName:"span",className:"mspace",style:{marginRight:"0.2778em"}}),(0,n.kt)("span",{parentName:"span",className:"mrel"},"="),(0,n.kt)("span",{parentName:"span",className:"mspace",style:{marginRight:"0.2778em"}})),(0,n.kt)("span",{parentName:"span",className:"base"},(0,n.kt)("span",{parentName:"span",className:"strut",style:{height:"1.4133em",verticalAlign:"-0.4811em"}}),(0,n.kt)("span",{parentName:"span",className:"mord"},(0,n.kt)("span",{parentName:"span",className:"mopen nulldelimiter"}),(0,n.kt)("span",{parentName:"span",className:"mfrac"},(0,n.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,n.kt)("span",{parentName:"span",className:"vlist-r"},(0,n.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.9322em"}},(0,n.kt)("span",{parentName:"span",style:{top:"-2.655em"}},(0,n.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,n.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.13889em"}},"T"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"t"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"a"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.01968em"}},"l"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"n"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"u"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"mb"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.02778em"}},"er"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10764em"}},"f"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"p"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"re"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"d"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"i"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"c"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"t"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"i"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"n"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"s")))),(0,n.kt)("span",{parentName:"span",style:{top:"-3.23em"}},(0,n.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,n.kt)("span",{parentName:"span",className:"frac-line",style:{borderBottomWidth:"0.04em"}})),(0,n.kt)("span",{parentName:"span",style:{top:"-3.4461em"}},(0,n.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,n.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10903em"}},"N"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"u"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"mb"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.02778em"}},"er"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10764em"}},"f"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"correc"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"t"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"p"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"re"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"d"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"i"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"c"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"t"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"i"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"n"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"s"))))),(0,n.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,n.kt)("span",{parentName:"span",className:"vlist-r"},(0,n.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.4811em"}},(0,n.kt)("span",{parentName:"span"}))))),(0,n.kt)("span",{parentName:"span",className:"mclose nulldelimiter"})))))),(0,n.kt)("p",null,"\nIn RS Metrics the computation is determined by the following formula:\n",(0,n.kt)("span",{parentName:"p",className:"math math-inline"},(0,n.kt)("span",{parentName:"span",className:"katex"},(0,n.kt)("span",{parentName:"span",className:"katex-mathml"},(0,n.kt)("math",{parentName:"span",xmlns:"http://www.w3.org/1998/Math/MathML"},(0,n.kt)("semantics",{parentName:"math"},(0,n.kt)("mrow",{parentName:"semantics"},(0,n.kt)("mi",{parentName:"mrow"},"A"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"u"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"a"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"y"),(0,n.kt)("mo",{parentName:"mrow"},"="),(0,n.kt)("mfrac",{parentName:"mrow"},(0,n.kt)("mrow",{parentName:"mfrac"},(0,n.kt)("mi",{parentName:"mrow"},"N"),(0,n.kt)("mi",{parentName:"mrow"},"u"),(0,n.kt)("mi",{parentName:"mrow"},"m"),(0,n.kt)("mi",{parentName:"mrow"},"b"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"f"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"t"),(0,n.kt)("mi",{parentName:"mrow"},"l"),(0,n.kt)("mi",{parentName:"mrow"},"y"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"m"),(0,n.kt)("mi",{parentName:"mrow"},"m"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"n"),(0,n.kt)("mi",{parentName:"mrow"},"d"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"d"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"s"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"v"),(0,n.kt)("mi",{parentName:"mrow"},"i"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"s")),(0,n.kt)("mrow",{parentName:"mfrac"},(0,n.kt)("mi",{parentName:"mrow"},"T"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"t"),(0,n.kt)("mi",{parentName:"mrow"},"a"),(0,n.kt)("mi",{parentName:"mrow"},"l"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"n"),(0,n.kt)("mi",{parentName:"mrow"},"u"),(0,n.kt)("mi",{parentName:"mrow"},"m"),(0,n.kt)("mi",{parentName:"mrow"},"b"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"o"),(0,n.kt)("mi",{parentName:"mrow"},"f"),(0,n.kt)("mtext",{parentName:"mrow"},"\u2005\u200a"),(0,n.kt)("mi",{parentName:"mrow"},"s"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"r"),(0,n.kt)("mi",{parentName:"mrow"},"v"),(0,n.kt)("mi",{parentName:"mrow"},"i"),(0,n.kt)("mi",{parentName:"mrow"},"c"),(0,n.kt)("mi",{parentName:"mrow"},"e"),(0,n.kt)("mi",{parentName:"mrow"},"s")))),(0,n.kt)("annotation",{parentName:"semantics",encoding:"application/x-tex"},"Accuracy=\\frac{Number\\;of\\;correctly\\;recommended\\;services}{Total\\;number\\;of\\;services}")))),(0,n.kt)("span",{parentName:"span",className:"katex-html","aria-hidden":"true"},(0,n.kt)("span",{parentName:"span",className:"base"},(0,n.kt)("span",{parentName:"span",className:"strut",style:{height:"0.8778em",verticalAlign:"-0.1944em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal"},"A"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal"},"cc"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal"},"u"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.02778em"}},"r"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal"},"a"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal",style:{marginRight:"0.03588em"}},"cy"),(0,n.kt)("span",{parentName:"span",className:"mspace",style:{marginRight:"0.2778em"}}),(0,n.kt)("span",{parentName:"span",className:"mrel"},"="),(0,n.kt)("span",{parentName:"span",className:"mspace",style:{marginRight:"0.2778em"}})),(0,n.kt)("span",{parentName:"span",className:"base"},(0,n.kt)("span",{parentName:"span",className:"strut",style:{height:"1.4133em",verticalAlign:"-0.4811em"}}),(0,n.kt)("span",{parentName:"span",className:"mord"},(0,n.kt)("span",{parentName:"span",className:"mopen nulldelimiter"}),(0,n.kt)("span",{parentName:"span",className:"mfrac"},(0,n.kt)("span",{parentName:"span",className:"vlist-t vlist-t2"},(0,n.kt)("span",{parentName:"span",className:"vlist-r"},(0,n.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.9322em"}},(0,n.kt)("span",{parentName:"span",style:{top:"-2.655em"}},(0,n.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,n.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.13889em"}},"T"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"t"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"a"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.01968em"}},"l"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"n"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"u"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"mb"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.02778em"}},"er"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10764em"}},"f"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.02778em"}},"ser"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03588em"}},"v"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"i"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"ces")))),(0,n.kt)("span",{parentName:"span",style:{top:"-3.23em"}},(0,n.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,n.kt)("span",{parentName:"span",className:"frac-line",style:{borderBottomWidth:"0.04em"}})),(0,n.kt)("span",{parentName:"span",style:{top:"-3.4461em"}},(0,n.kt)("span",{parentName:"span",className:"pstrut",style:{height:"3em"}}),(0,n.kt)("span",{parentName:"span",className:"sizing reset-size6 size3 mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mtight"},(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10903em"}},"N"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"u"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"mb"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.02778em"}},"er"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"o"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.10764em"}},"f"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"correc"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.01968em"}},"tl"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03588em"}},"y"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"reco"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"mm"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"e"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"n"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"d"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"e"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"d"),(0,n.kt)("span",{parentName:"span",className:"mspace mtight",style:{marginRight:"0.3253em"}}),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.02778em"}},"ser"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight",style:{marginRight:"0.03588em"}},"v"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"i"),(0,n.kt)("span",{parentName:"span",className:"mord mathnormal mtight"},"ces"))))),(0,n.kt)("span",{parentName:"span",className:"vlist-s"},"\u200b")),(0,n.kt)("span",{parentName:"span",className:"vlist-r"},(0,n.kt)("span",{parentName:"span",className:"vlist",style:{height:"0.4811em"}},(0,n.kt)("span",{parentName:"span"}))))),(0,n.kt)("span",{parentName:"span",className:"mclose nulldelimiter"})))))),"where correctness is defined as if the service is both accessed by the user and also it is recommended by the RS")),(0,n.kt)("h2",{id:"output"},"Output"),(0,n.kt)("table",null,(0,n.kt)("thead",{parentName:"table"},(0,n.kt)("tr",{parentName:"thead"},(0,n.kt)("th",{parentName:"tr",align:null},"Type"),(0,n.kt)("th",{parentName:"tr",align:null},"Float"))),(0,n.kt)("tbody",{parentName:"table"},(0,n.kt)("tr",{parentName:"tbody"},(0,n.kt)("td",{parentName:"tr",align:null},"Min"),(0,n.kt)("td",{parentName:"tr",align:null},"0")),(0,n.kt)("tr",{parentName:"tbody"},(0,n.kt)("td",{parentName:"tr",align:null},"Max"),(0,n.kt)("td",{parentName:"tr",align:null},"1")))),(0,n.kt)("admonition",{type:"info"},(0,n.kt)("p",{parentName:"admonition"},"A value of 1, indicates that the RS model got all the predictions right, and a value of 0 indicates that the RS model did not make a single correct prediction.")),(0,n.kt)("h2",{id:"prerequisites"},"Prerequisites:"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},"recommendations without anonymous users"),(0,n.kt)("li",{parentName:"ul"},"all available users (with their accessed services)"),(0,n.kt)("li",{parentName:"ul"},"all available services")),(0,n.kt)("h2",{id:"process-flow"},"Process Flow:"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("h3",{parentName:"li",id:"clean-up"},"Clean up"),'Recommendations clean up; entries removal where users or services are not found in "users" or "services" accordingly'),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("h3",{parentName:"li",id:"vector-creation-of-the-accessed-services"},"Vector creation of the Accessed Services"),"For each user create a vector at the size of the number of the services, and assign a binary value for each service with a value of 1 if it is found in the user's accessed services, or 0 if it is not"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("h3",{parentName:"li",id:"vector-creation-of-the-recommended-services"},"Vector creation of the Recommended Services"),"For each user create a vector at the size of the number of the services, and assign a binary value for each service with a value of 1 if it is recommended to the user, or 0 if it is not"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("h3",{parentName:"li",id:"accuracy-score-computation"},"Accuracy score computation"),"For each user compute the average value of the difference vector; a vector which states True if service is found in both accessed and recommended vectors or False if it is not"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("h3",{parentName:"li",id:"mean-value-of-accuracy-score"},"Mean value of Accuracy score"),"Computation of the overall value by calculating the mean value of each user's accuracy score")))}c.isMDXComponent=!0}}]);