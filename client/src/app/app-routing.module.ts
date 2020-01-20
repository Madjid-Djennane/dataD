import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TraficComponent } from './trafic/trafic.component';
import { IpsComponent } from './ips/ips.component';


const routes: Routes = [
  {path: '', redirectTo: 'trafic', pathMatch: 'full'},
  {path : 'trafic', component: TraficComponent},
  {path : 'ips', component: IpsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
