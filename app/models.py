from matplotlib.collections import Collection
from flask import Flask
from flask_login import UserMixin
from app import app, Base, Column, Integer, String
from sqlalchemy import Column, String, Integer, DateTime, BLOB

class Usuario(UserMixin, Base):
  __tablename__ = 'usuario'

  id=Column(Integer,primary_key=True)
  permissoes_id=Column(Integer,nullable=False)
  nome=Column(String(25),nullable=False)
  login=Column(String(25), nullable=False)
  email=Column(String(50),nullable=False)
  senha=Column(String(50), nullable=False)

  def __repr__(self):
    return f"<User nome={self.nome} login={self.login} email={self.email}"

class Fornecedor(UserMixin, Base):
  __tablename__ = 'fornecedor'
  
  id=Column(Integer,primary_key=True)
  nome=Column(String(50),nullable=False)
  nome_fantasia=Column(String(50),nullable=False)
  cnpj=Column(String(25),nullable=False)
  logradouro=Column(String(50),nullable=False)
  bairro=Column(String(25),nullable=False)
  cidade=Column(String(25),nullable=False)
  numero=Column(Integer, nullable=False)
  cep=Column(Integer,nullable=False)
  uf=Column(String(2),nullable=False)
  nome_contato1=Column(String(20),nullable=False)
  nome_contato2=Column(String(20),nullable=False)
  email_contato2=Column(String(20),nullable=False)
  email_contato2=Column(String(20),nullable=False)
  fone_contato2=Column(String(10),nullable=False)
  fone_contato2=Column(String(10),nullable=False)

class Material(UserMixin, Base):
  __tablename__ = 'material'

  id=Column(Integer,primary_key=True)
  fabricanteId=Column(Integer,nullable=False)
  tipoId=Column(Integer,nullable=False)
  grupoId=Column(Integer,nullable=False)
  modelo=Column(String(50),nullable=False)
  ncm=Column(String(50),nullable=False)
  estoqueMin=Column(Integer,nullable=False)
  posicaoEstoque=Column(String(50),nullable=False)
  foto=Column(BLOB,nullable=False)
  possuiNumSerie=Column(Integer,nullable=False)

class Permissoes(UserMixin, Base):
  __tablename__ = 'permissoes'

  id=Column(Integer,primary_key=True)
  descricao=Column(String(50),nullable=False)